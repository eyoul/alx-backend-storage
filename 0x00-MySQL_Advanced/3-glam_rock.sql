-- Column names must be: band_name and lifespan (in years)
-- attributes formed and split for computing the lifespan

SELECT band_name, COALESCE(split, '2020') - formed as lifespanFROM
metal_bands WHERE style LIKE '%Glam rock%' ORDER BY lifespan DESC;