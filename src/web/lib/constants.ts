export const CHAINS = ["Ethereum", "Arbitrum", "Polygon", "BSC", "Avalanche", "Optimism", "Fantom", "Solana"] as const
export const CATEGORIES = ["Lending", "DEX", "Yield", "Bridge", "Liquid Staking", "CDP", "Derivatives", "Yield Aggregator"] as const
export const RISK_LEVELS = ["low", "medium", "high", "critical"] as const

export const RISK_COLORS = {
  low: "#4ade80",
  medium: "#facc15",
  high: "#fb923c",
  critical: "#ef4444",
} as const

export const WEIGHTS = {
  tvl_stability: 0.30,
  apy_sustainability: 0.20,
  contract_security: 0.25,
  governance_distribution: 0.15,
  liquidity_depth: 0.10,
} as const
