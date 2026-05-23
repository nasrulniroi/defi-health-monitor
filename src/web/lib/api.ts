const API_BASE = process.env.NEXT_PUBLIC_API_URL || "/api"

export async function fetchProtocols() {
  const res = await fetch(`${API_BASE}/protocols`)
  return res.json()
}

export async function fetchProtocol(id: string) {
  const res = await fetch(`${API_BASE}/protocols/${id}`)
  return res.json()
}

export async function fetchAlerts() {
  const res = await fetch(`${API_BASE}/alerts`)
  return res.json()
}

export async function fetchRiskOverview() {
  const res = await fetch(`${API_BASE}/risk/overview`)
  return res.json()
}
