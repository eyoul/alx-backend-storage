-- This SQL script select band_name, and lifespan column which is difference

SELECT band_name, COALESCE(split, 2020) - formed as lifespan FROM
metal_bands WHERE style LIKE '%Glam rock%' ORDER BY lifespan DESC;
