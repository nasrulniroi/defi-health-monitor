import { describe, it, expect } from 'vitest'

describe('Dashboard', () => {
  it('formats TVL correctly', () => {
    const formatTVL = (value: number) => {
      if (value >= 1e12) return `$${(value / 1e12).toFixed(2)}T`
      if (value >= 1e9) return `$${(value / 1e9).toFixed(2)}B`
      if (value >= 1e6) return `$${(value / 1e6).toFixed(2)}M`
      return `$${value}`
    }
    expect(formatTVL(12500000000)).toBe('$12.50B')
    expect(formatTVL(500000000)).toBe('$500.00M')
  })

  it('categorizes risk levels', () => {
    const getRiskLevel = (score: number) => {
      if (score >= 75) return 'low'
      if (score >= 50) return 'medium'
      if (score >= 25) return 'high'
      return 'critical'
    }
    expect(getRiskLevel(85)).toBe('low')
    expect(getRiskLevel(60)).toBe('medium')
    expect(getRiskLevel(35)).toBe('high')
    expect(getRiskLevel(10)).toBe('critical')
  })
})
