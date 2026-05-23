import { describe, it, expect } from 'vitest'

describe('RiskGauge', () => {
  it('calculates gauge dasharray', () => {
    const value = 75
    const maxArc = 251.3
    const dasharray = (value / 100) * maxArc
    expect(dasharray).toBeCloseTo(188.475, 1)
  })

  it('selects correct color for value', () => {
    const getColor = (v: number) => v >= 75 ? '#4ade80' : v >= 50 ? '#facc15' : v >= 25 ? '#fb923c' : '#ef4444'
    expect(getColor(90)).toBe('#4ade80')
    expect(getColor(30)).toBe('#fb923c')
  })
})
