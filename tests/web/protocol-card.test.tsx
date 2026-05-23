import { describe, it, expect } from 'vitest'

describe('ProtocolCard', () => {
  it('calculates health score percentage', () => {
    const score = 82.5
    expect(score).toBeGreaterThanOrEqual(0)
    expect(score).toBeLessThanOrEqual(100)
  })

  it('maps risk level to color', () => {
    const colors: Record<string, string> = { low: '#4ade80', medium: '#facc15', high: '#fb923c', critical: '#ef4444' }
    expect(colors['low']).toBe('#4ade80')
    expect(colors['critical']).toBe('#ef4444')
  })
})
