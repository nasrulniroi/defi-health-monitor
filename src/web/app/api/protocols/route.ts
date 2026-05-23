import { NextResponse } from "next/server"

export async function GET() {
  try {
    const res = await fetch("http://localhost:8000/api/protocols")
    const data = await res.json()
    return NextResponse.json(data)
  } catch {
    return NextResponse.json({ data: [], error: "Engine unavailable" }, { status: 503 })
  }
}
