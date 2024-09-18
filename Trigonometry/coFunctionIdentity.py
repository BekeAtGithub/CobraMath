'''
Co-function identities in trigonometry state that certain trigonometric functions of complementary angles are equal. The primary co-function identities are:
#θ = theta , not a zero 
    sin⁡(90∘−θ)=cos⁡(θ)sin(90∘−θ)=cos(θ)
    cos⁡(90∘−θ)=sin⁡(θ)cos(90∘−θ)=sin(θ)
    tan⁡(90∘−θ)=cot⁡(θ)tan(90∘−θ)=cot(θ)
    cot⁡(90∘−θ)=tan⁡(θ)cot(90∘−θ)=tan(θ)
    sec⁡(90∘−θ)=csc⁡(θ)sec(90∘−θ)=csc(θ) 
    csc⁡(90∘−θ)=sec⁡(θ)csc(90∘−θ)=sec(θ)

Here's a Python script to verify these co-function identities for a given angle θθ:
'''


import math

def verify_co_function_identities(angle_degrees):
    # Convert angle from degrees to radians
    angle_radians = math.radians(angle_degrees)
    complementary_angle_radians = math.radians(90 - angle_degrees)
    
    # Calculate trigonometric functions for the given angle
    sin_theta = math.sin(angle_radians)
    cos_theta = math.cos(angle_radians)
    tan_theta = math.tan(angle_radians)
    cot_theta = 1 / tan_theta if tan_theta != 0 else float('inf')
    sec_theta = 1 / cos_theta if cos_theta != 0 else float('inf')
    csc_theta = 1 / sin_theta if sin_theta != 0 else float('inf')
    
    # Calculate trigonometric functions for the complementary angle
    sin_complementary = math.sin(complementary_angle_radians)
    cos_complementary = math.cos(complementary_angle_radians)
    tan_complementary = math.tan(complementary_angle_radians)
    cot_complementary = 1 / tan_complementary if tan_complementary != 0 else float('inf')
    sec_complementary = 1 / cos_complementary if cos_complementary != 0 else float('inf')
    csc_complementary = 1 / sin_complementary if sin_complementary != 0 else float('inf')
    
    # Verify the identities
    results = { #θ = theta , not a zero
        'sin(90° - θ) == cos(θ)': math.isclose(sin_complementary, cos_theta, rel_tol=1e-9),
        'cos(90° - θ) == sin(θ)': math.isclose(cos_complementary, sin_theta, rel_tol=1e-9),
        'tan(90° - θ) == cot(θ)': math.isclose(tan_complementary, cot_theta, rel_tol=1e-9),
        'cot(90° - θ) == tan(θ)': math.isclose(cot_complementary, tan_theta, rel_tol=1e-9),
        'sec(90° - θ) == csc(θ)': math.isclose(sec_complementary, csc_theta, rel_tol=1e-9),
        'csc(90° - θ) == sec(θ)': math.isclose(csc_complementary, sec_theta, rel_tol=1e-9)
    }
    
    return results

# Example usage
angle = 30  # degrees
results = verify_co_function_identities(angle)

for identity, verified in results.items():
    print(f"{identity}: {'Verified' if verified else 'Not Verified'}")
'''
Guide:

    angle_degrees: The angle in degrees for which the identities are verified.
    angle_radians: The angle in radians, which is used for trigonometric calculations in Python.
    complementary_angle_radians: The complementary angle (90∘−θ90∘−θ) in radians.
    sin_theta, cos_theta, etc.: Trigonometric functions of the given angle.
    sin_complementary, cos_complementary, etc.: Trigonometric functions of the complementary angle.
    Verification: Each identity is verified by checking if the trigonometric function of the complementary angle is close to the corresponding function of the original angle, within a relative tolerance.
'''
 
