'''
The product-to-sum and sum-to-product identities in trigonometry are used to transform products of trigonometric functions into sums or differences and vice versa.
Product-to-Sum Identities:

    sin⁡(a)sin⁡(b)=12[cos⁡(a−b)−cos⁡(a+b)]sin(a)sin(b)=21​[cos(a−b)−cos(a+b)]
    cos⁡(a)cos⁡(b)=12[cos⁡(a+b)+cos⁡(a−b)]cos(a)cos(b)=21​[cos(a+b)+cos(a−b)]
    sin⁡(a)cos⁡(b)=12[sin⁡(a+b)+sin⁡(a−b)]sin(a)cos(b)=21​[sin(a+b)+sin(a−b)]

Sum-to-Product Identities:

    sin⁡(a)±sin⁡(b)=2sin⁡(a±b2)cos⁡(a∓b2)sin(a)±sin(b)=2sin(2a±b​)cos(2a∓b​)
    cos⁡(a)+cos⁡(b)=2cos⁡(a+b2)cos⁡(a−b2)cos(a)+cos(b)=2cos(2a+b​)cos(2a−b​)
    cos⁡(a)−cos⁡(b)=−2sin⁡(a+b2)sin⁡(a−b2)cos(a)−cos(b)=−2sin(2a+b​)sin(2a−b​)

Here's a Python script that calculates and verifies these identities for given angles aa and bb:

'''

import math

def verify_product_to_sum_identities(angle_a_degrees, angle_b_degrees):
    # Convert angles from degrees to radians
    angle_a_radians = math.radians(angle_a_degrees)
    angle_b_radians = math.radians(angle_b_degrees)
    
    # Calculate trigonometric functions for the given angles
    sin_a = math.sin(angle_a_radians)
    cos_a = math.cos(angle_a_radians)
    sin_b = math.sin(angle_b_radians)
    cos_b = math.cos(angle_b_radians)
    
    # Calculate product-to-sum identities
    sin_sin_identity = 0.5 * (math.cos(angle_a_radians - angle_b_radians) - math.cos(angle_a_radians + angle_b_radians))
    cos_cos_identity = 0.5 * (math.cos(angle_a_radians + angle_b_radians) + math.cos(angle_a_radians - angle_b_radians))
    sin_cos_identity = 0.5 * (math.sin(angle_a_radians + angle_b_radians) + math.sin(angle_a_radians - angle_b_radians))
    
    # Verify the identities
    results_product_to_sum = {
        'sin(a)sin(b) = 0.5[cos(a - b) - cos(a + b)]': math.isclose(sin_a * sin_b, sin_sin_identity, rel_tol=1e-9),
        'cos(a)cos(b) = 0.5[cos(a + b) + cos(a - b)]': math.isclose(cos_a * cos_b, cos_cos_identity, rel_tol=1e-9),
        'sin(a)cos(b) = 0.5[sin(a + b) + sin(a - b)]': math.isclose(sin_a * cos_b, sin_cos_identity, rel_tol=1e-9),
    }
    
    return results_product_to_sum

def verify_sum_to_product_identities(angle_a_degrees, angle_b_degrees):
    # Convert angles from degrees to radians
    angle_a_radians = math.radians(angle_a_degrees)
    angle_b_radians = math.radians(angle_b_degrees)
    
    # Calculate trigonometric functions for the given angles
    sin_a = math.sin(angle_a_radians)
    cos_a = math.cos(angle_a_radians)
    sin_b = math.sin(angle_b_radians)
    cos_b = math.cos(angle_b_radians)
    
    # Calculate sum-to-product identities
    sin_sum_identity = 2 * math.sin((angle_a_radians + angle_b_radians) / 2) * math.cos((angle_a_radians - angle_b_radians) / 2)
    sin_diff_identity = 2 * math.sin((angle_a_radians - angle_b_radians) / 2) * math.cos((angle_a_radians + angle_b_radians) / 2)
    cos_sum_identity = 2 * math.cos((angle_a_radians + angle_b_radians) / 2) * math.cos((angle_a_radians - angle_b_radians) / 2)
    cos_diff_identity = -2 * math.sin((angle_a_radians + angle_b_radians) / 2) * math.sin((angle_a_radians - angle_b_radians) / 2)
    
    # Verify the identities
    results_sum_to_product = {
        'sin(a) + sin(b) = 2sin((a + b)/2)cos((a - b)/2)': math.isclose(sin_a + sin_b, sin_sum_identity, rel_tol=1e-9),
        'sin(a) - sin(b) = 2sin((a - b)/2)cos((a + b)/2)': math.isclose(sin_a - sin_b, sin_diff_identity, rel_tol=1e-9),
        'cos(a) + cos(b) = 2cos((a + b)/2)cos((a - b)/2)': math.isclose(cos_a + cos_b, cos_sum_identity, rel_tol=1e-9),
        'cos(a) - cos(b) = -2sin((a + b)/2)sin((a - b)/2)': math.isclose(cos_a - cos_b, cos_diff_identity, rel_tol=1e-9),
    }
    
    return results_sum_to_product

# Example usage
angle_a = 45  # degrees
angle_b = 30  # degrees

results_product_to_sum = verify_product_to_sum_identities(angle_a, angle_b)
results_sum_to_product = verify_sum_to_product_identities(angle_a, angle_b)

print("Product-to-Sum Identities:")
for identity, verified in results_product_to_sum.items():
    print(f"{identity}: {'Verified' if verified else 'Not Verified'}")

print("\nSum-to-Product Identities:")
for identity, verified in results_sum_to_product.items():
    print(f"{identity}: {'Verified' if verified else 'Not Verified'}")
'''
Explanation:

    angle_a_degrees, angle_b_degrees: The angles aa and bb in degrees for which the identities are verified.
    angle_a_radians, angle_b_radians: The angles in radians, which are used for trigonometric calculations in Python.
    sin_a, cos_a, sin_b, cos_b: The sine and cosine of angles aa and bb, respectively.
    Product-to-Sum Identities: Calculated using the provided formulas.
    Sum-to-Product Identities: Calculated using the provided formulas.
    Verification: Each identity is verified by checking if the calculated values are close to the values obtained using the math functions, within a relative tolerance.
'''
