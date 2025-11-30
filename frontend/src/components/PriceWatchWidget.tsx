import React, { useState } from 'react';
import axios from 'axios';
import { Tag, Plane, CheckCircle, AlertCircle } from 'lucide-react';
import { motion } from 'framer-motion';

const PriceWatchWidget: React.FC = () => {
    const [destination, setDestination] = useState('');
    const [targetPrice, setTargetPrice] = useState('');
    const [status, setStatus] = useState<'idle' | 'loading' | 'success' | 'error'>('idle');
    const [operationId, setOperationId] = useState<string | null>(null);

    const startWatch = async (e: React.FormEvent) => {
        e.preventDefault();
        if (!destination || !targetPrice) return;

        setStatus('loading');
        try {
            const response = await axios.post('http://localhost:8000/start-price-watch', {
                user_id: 'test_user',
                destination,
                target_price: parseFloat(targetPrice),
            });
            setOperationId(response.data.operation_id);
            setStatus('success');
            // Reset form after delay
            setTimeout(() => {
                setStatus('idle');
                setDestination('');
                setTargetPrice('');
            }, 3000);
        } catch (error) {
            console.error('Error starting price watch:', error);
            setStatus('error');
        }
    };

    return (
        <motion.div
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            className="bg-white dark:bg-gray-800 p-6 rounded-xl shadow-lg border border-gray-200 dark:border-gray-700 w-full max-w-sm"
        >
            <div className="flex items-center gap-3 mb-6">
                <div className="p-2 bg-purple-100 dark:bg-purple-900/30 rounded-lg">
                    <Tag className="w-6 h-6 text-purple-600 dark:text-purple-400" />
                </div>
                <div>
                    <h3 className="text-lg font-semibold text-gray-900 dark:text-gray-100">Price Watch</h3>
                    <p className="text-sm text-gray-500 dark:text-gray-400">Track flight prices automatically</p>
                </div>
            </div>

            <form onSubmit={startWatch} className="space-y-4">
                <div>
                    <label className="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-1">
                        Destination
                    </label>
                    <div className="relative">
                        <Plane className="absolute left-3 top-1/2 -translate-y-1/2 w-4 h-4 text-gray-400" />
                        <input
                            type="text"
                            value={destination}
                            onChange={(e) => setDestination(e.target.value)}
                            placeholder="e.g., Paris, Tokyo"
                            className="w-full pl-10 pr-4 py-2 rounded-lg border border-gray-300 dark:border-gray-600 bg-gray-50 dark:bg-gray-900 text-gray-900 dark:text-gray-100 focus:ring-2 focus:ring-purple-500 focus:border-transparent outline-none transition-all"
                        />
                    </div>
                </div>

                <div>
                    <label className="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-1">
                        Target Price ($)
                    </label>
                    <div className="relative">
                        <span className="absolute left-3 top-1/2 -translate-y-1/2 text-gray-400">$</span>
                        <input
                            type="number"
                            value={targetPrice}
                            onChange={(e) => setTargetPrice(e.target.value)}
                            placeholder="500"
                            className="w-full pl-8 pr-4 py-2 rounded-lg border border-gray-300 dark:border-gray-600 bg-gray-50 dark:bg-gray-900 text-gray-900 dark:text-gray-100 focus:ring-2 focus:ring-purple-500 focus:border-transparent outline-none transition-all"
                        />
                    </div>
                </div>

                <button
                    type="submit"
                    disabled={status === 'loading'}
                    className={`w-full py-2 px-4 rounded-lg font-medium text-white transition-all ${status === 'loading'
                            ? 'bg-purple-400 cursor-not-allowed'
                            : 'bg-purple-600 hover:bg-purple-700 shadow-md hover:shadow-lg'
                        }`}
                >
                    {status === 'loading' ? 'Starting Watch...' : 'Start Tracking'}
                </button>

                {status === 'success' && (
                    <motion.div
                        initial={{ opacity: 0, height: 0 }}
                        animate={{ opacity: 1, height: 'auto' }}
                        className="flex items-center gap-2 text-green-600 dark:text-green-400 text-sm bg-green-50 dark:bg-green-900/20 p-3 rounded-lg"
                    >
                        <CheckCircle className="w-4 h-4" />
                        <span>Tracking started! ID: {operationId}</span>
                    </motion.div>
                )}

                {status === 'error' && (
                    <motion.div
                        initial={{ opacity: 0, height: 0 }}
                        animate={{ opacity: 1, height: 'auto' }}
                        className="flex items-center gap-2 text-red-600 dark:text-red-400 text-sm bg-red-50 dark:bg-red-900/20 p-3 rounded-lg"
                    >
                        <AlertCircle className="w-4 h-4" />
                        <span>Failed to start tracking. Try again.</span>
                    </motion.div>
                )}
            </form>
        </motion.div>
    );
};

export default PriceWatchWidget;
