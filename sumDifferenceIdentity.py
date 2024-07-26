'''
The sum and difference identities for trigonometric functions are used to express the trigonometric functions of sums or differences of angles in terms of the functions of the individual angles. Here are the sum and difference identities:

    sin⁡(a±b)=sin⁡(a)cos⁡(b)±cos⁡(a)sin⁡(b)sin(a±b)=sin(a)cos(b)±cos(a)sin(b)
    cos⁡(a±b)=cos⁡(a)cos⁡(b)∓sin⁡(a)sin⁡(b)cos(a±b)=cos(a)cos(b)∓sin(a)sin(b)
    tan⁡(a±b)=tan⁡(a)±tan⁡(b)1∓tan⁡(a)tan⁡(b)tan(a±b)=1∓tan(a)tan(b)tan(a)±tan(b)​

Here is a Python script that calculates and verifies these sum and difference identities for given angles aa and bb:
'''


import math

def verify_sum_and_difference_identities(angle_a_degrees, angle_b_degrees):
    # Convert angles from degrees to radians
    angle_a_radians = math.radians(angle_a_degrees)
    angle_b_radians = math.radians(angle_b_degrees)
    
    # Calculate trigonometric functions for the given angles
    sin_a = math.sin(angle_a_radians)
    cos_a = math.cos(angle_a_radians)
    tan_a = math.tan(angle_a_radians)
    
    sin_b = math.sin(angle_b_radians)
    cos_b = math.cos(angle_b_radians)
    tan_b = math.tan(angle_b_radians)
    
    # Calculate sin(a ± b)
    sin_a_plus_b = math.sin(angle_a_radians + angle_b_radians)
    sin_a_minus_b = math.sin(angle_a_radians - angle_b_radians)
    
    sin_sum_identity = sin_a * cos_b + cos_a * sin_b
    sin_diff_identity = sin_a * cos_b - cos_a * sin_b
    
    # Calculate cos(a ± b)
    cos_a_plus_b = math.cos(angle_a_radians + angle_b_radians)
    cos_a_minus_b = math.cos(angle_a_radians - angle_b_radians)
    
    cos_sum_identity = cos_a * cos_b - sin_a * sin_b
    cos_diff_identity = cos_a * cos_b + sin_a * sin_b
    
    # Calculate tan(a ± b)
    tan_a_plus_b = math.tan(angle_a_radians + angle_b_radians)
    tan_a_minus_b = math.tan(angle_a_radians - angle_b_radians)
    
    tan_sum_identity = (tan_a + tan_b) / (1 - tan_a * tan_b)
    tan_diff_identity = (tan_a - tan_b) / (1 + tan_a * tan_b)
    
    # Verify the identities
    results = {
        'sin(a + b) = sin(a)cos(b) + cos(a)sin(b)': math.isclose(sin_a_plus_b, sin_sum_identity, rel_tol=1e-9),
        'sin(a - b) = sin(a)cos(b) - cos(a)sin(b)': math.isclose(sin_a_minus_b, sin_diff_identity, rel_tol=1e-9),
        'cos(a + b) = cos(a)cos(b) - sin(a)sin(b)': math.isclose(cos_a_plus_b, cos_sum_identity, rel_tol=1e-9),
        'cos(a - b) = cos(a)cos(b) + sin(a)sin(b)': math.isclose(cos_a_minus_b, cos_diff_identity, rel_tol=1e-9),
        'tan(a + b) = (tan(a) + tan(b)) / (1 - tan(a)tan(b))': math.isclose(tan_a_plus_b, tan_sum_identity, rel_tol=1e-9),
        'tan(a - b) = (tan(a) - tan(b)) / (1 + tan(a)tan(b))': math.isclose(tan_a_minus_b, tan_diff_identity, rel_tol=1e-9)
    }
    
    return results

# Example usage
angle_a = 45  # degrees
angle_b = 30  # degrees
results = verify_sum_and_difference_identities(angle_a, angle_b)

for identity, verified in results.items():
    print(f"{identity}: {'Verified' if verified else 'Not Verified'}")
'''
Explanation:

    angle_a_degrees, angle_b_degrees: The angles aa and bb in degrees for which the identities are verified.
    angle_a_radians, angle_b_radians: The angles in radians, which are used for trigonometric calculations in Python.
    sin_a, cos_a, tan_a, sin_b, cos_b, tan_b: The sine, cosine, and tangent of angles aa and bb, respectively.
    sin_a_plus_b, sin_a_minus_b: The sine of the sum and difference of angles aa and bb.
    cos_a_plus_b, cos_a_minus_b: The cosine of the sum and difference of angles aa and bb.
    tan_a_plus_b, tan_a_minus_b: The tangent of the sum and difference of angles aa and bb.
    Verification: Each identity is verified by checking if the calculated values are close to the values obtained using the math functions, within a relative tolerance.
'''
