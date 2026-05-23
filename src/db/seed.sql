INSERT INTO protocols (slug, name, chain, category, tvl) VALUES
('aave', 'Aave', 'Multi', 'Lending', 12500000000),
('lido', 'Lido', 'Ethereum', 'Liquid Staking', 28000000000),
('uniswap', 'Uniswap', 'Multi', 'DEX', 5200000000),
('makerdao', 'MakerDAO', 'Ethereum', 'CDP', 8300000000),
('compound', 'Compound', 'Multi', 'Lending', 2800000000),
('curve', 'Curve', 'Multi', 'DEX', 3100000000),
('gmx', 'GMX', 'Arbitrum', 'Derivatives', 650000000),
('pendle', 'Pendle', 'Multi', 'Yield', 4200000000)
ON CONFLICT (slug) DO NOTHING;
