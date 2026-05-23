"use client"
import { useEffect, useState } from "react"
import { ProtocolCard } from "../../components/protocol-card"

export default function ProtocolsPage() {
  const [protocols, setProtocols] = useState<any[]>([])
  const [filter, setFilter] = useState("all")
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    fetch("/api/protocols").then(r => r.json()).then(d => { setProtocols(d.data || []) }).finally(() => setLoading(false))
  }, [])

  const filtered = filter === "all" ? protocols : protocols.filter(p => p.risk_level === filter)

  return (
    <div className="space-y-6">
      <h2 className="text-3xl font-bold">Protocol Explorer</h2>
      <div className="flex gap-2">
        {["all", "low", "medium", "high", "critical"].map(f => (
          <button key={f} onClick={() => setFilter(f)} className={`px-3 py-1.5 rounded-md text-sm capitalize ${filter === f ? "bg-primary text-primary-foreground" : "bg-muted text-muted-foreground hover:bg-accent"}`}>{f}</button>
        ))}
      </div>
      {loading ? <div>Loading...</div> : (
        <div className="grid grid-cols-3 gap-4">
          {filtered.map((p, i) => <ProtocolCard key={i} protocol={p} />)}
        </div>
      )}
    </div>
  )
}
