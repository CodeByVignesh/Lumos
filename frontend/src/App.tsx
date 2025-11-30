import ChatInterface from './components/ChatInterface';
import PriceWatchWidget from './components/PriceWatchWidget';
import { LayoutDashboard } from 'lucide-react';

function App() {
  return (
    <div className="h-screen w-screen bg-gray-100 dark:bg-gray-950 flex overflow-hidden">
      {/* Sidebar */}
      <aside className="w-80 bg-white dark:bg-gray-900 border-r border-gray-200 dark:border-gray-800 flex flex-col hidden md:flex">
        <div className="p-6 border-b border-gray-200 dark:border-gray-800">
          <h1 className="text-xl font-bold text-gray-900 dark:text-white tracking-tight flex items-center gap-2">
            <LayoutDashboard className="w-6 h-6 text-blue-600" />
            Lumos
          </h1>
        </div>

        <div className="flex-1 overflow-y-auto p-4 space-y-6">
          <PriceWatchWidget />

          <div className="bg-gray-50 dark:bg-gray-800/50 p-4 rounded-xl border border-gray-200 dark:border-gray-700">
            <h3 className="text-sm font-semibold text-gray-900 dark:text-gray-100 mb-2">
              Active Agents
            </h3>
            <div className="flex flex-col gap-2">
              <div className="flex items-center gap-2 text-sm text-gray-600 dark:text-gray-400">
                <div className="w-2 h-2 rounded-full bg-green-500"></div>
                Orchestrator
              </div>
              <div className="flex items-center gap-2 text-sm text-gray-600 dark:text-gray-400">
                <div className="w-2 h-2 rounded-full bg-gray-300 dark:bg-gray-600"></div>
                Travel Planner
              </div>
            </div>
          </div>
        </div>

        <div className="p-4 border-t border-gray-200 dark:border-gray-800">
          <div className="flex items-center gap-3 p-2 rounded-lg hover:bg-gray-100 dark:hover:bg-gray-800 cursor-pointer transition-colors">
            <div className="w-8 h-8 rounded-full bg-blue-100 dark:bg-blue-900 flex items-center justify-center text-blue-600 dark:text-blue-400 font-semibold">
              U
            </div>
            <div className="text-sm">
              <p className="font-medium text-gray-900 dark:text-gray-100">User</p>
              <p className="text-gray-500 dark:text-gray-400 text-xs">Pro Plan</p>
            </div>
          </div>
        </div>
      </aside>

      {/* Main Content */}
      <main className="flex-1 flex flex-col h-full relative">
        {/* Mobile Header */}
        <div className="md:hidden p-4 bg-white dark:bg-gray-900 border-b border-gray-200 dark:border-gray-800 flex items-center justify-between">
          <h1 className="text-lg font-bold text-gray-900 dark:text-white">Lumos</h1>
        </div>

        <div className="flex-1 flex flex-col h-full overflow-hidden">
          <ChatInterface />
        </div>
      </main>
    </div>
  );
}

export default App;
