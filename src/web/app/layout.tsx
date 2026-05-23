import type { Metadata } from "next"
import "../styles/globals.css"

export const metadata: Metadata = {
  title: "DeFi Protocol Health Monitor",
  description: "Real-time risk intelligence for DeFi protocols across 8+ blockchains",
}

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en" className="dark">
      <body className="min-h-screen bg-background antialiased">
        <div className="flex min-h-screen">
          <aside className="w-64 border-r border-border bg-card p-4">
            <h1 className="text-xl font-bold text-primary mb-6">DeFi Health</h1>
            <nav className="space-y-2">
              <a href="/" className="block px-3 py-2 rounded-md hover:bg-accent">Dashboard</a>
              <a href="/protocols" className="block px-3 py-2 rounded-md hover:bg-accent">Protocols</a>
              <a href="/alerts" className="block px-3 py-2 rounded-md hover:bg-accent">Alerts</a>
              <a href="/analytics" className="block px-3 py-2 rounded-md hover:bg-accent">Analytics</a>
            </nav>
          </aside>
          <main className="flex-1 p-6">{children}</main>
        </div>
      </body>
    </html>
  )
}
