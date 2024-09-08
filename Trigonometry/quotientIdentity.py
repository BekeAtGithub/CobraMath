''' 
The quotient identities are:

    tan⁡(θ)=sin⁡(θ)cos⁡(θ)tan(θ)=cos(θ)sin(θ)​
    cot⁡(θ)=cos⁡(θ)sin⁡(θ)cot(θ)=sin(θ)cos(θ)​

Here is a script that verifies these identities for a given angle θθ:
'''


import math

def verify_quotient_identities(angle_degrees):
    # Convert angle from degrees to radians
    angle_radians = math.radians(angle_degrees)
    
    # Calculate sin, cos, tan, and cot values
    sin_theta = math.sin(angle_radians)
    cos_theta = math.cos(angle_radians)
    
    # Avoid division by zero
    if cos_theta == 0:
        tan_theta = float('inf')
    else:
        tan_theta = sin_theta / cos_theta
    
    if sin_theta == 0:
        cot_theta = float('inf')
    else:
        cot_theta = cos_theta / sin_theta
    
    # Calculate tan and cot using math functions
    tan_func = math.tan(angle_radians)
    cot_func = 1 / tan_func if tan_func != 0 else float('inf')
    
    # Verify the identities
    tan_identity_verified = math.isclose(tan_theta, tan_func, rel_tol=1e-9)
    cot_identity_verified = math.isclose(cot_theta, cot_func, rel_tol=1e-9)
    
    return {
        'tan(theta)': tan_theta,
        'tan(theta) using math.tan': tan_func,
        'tan identity verified': tan_identity_verified,
        'cot(theta)': cot_theta,
        'cot(theta) using math.cot': cot_func,
        'cot identity verified': cot_identity_verified
    }

# Example usage
angle = 45  # degrees
results = verify_quotient_identities(angle)

for key, value in results.items():
    print(f"{key}: {value}")
'''
Explanation:

    angle_degrees: The angle in degrees for which the identities are verified.
    angle_radians: The angle in radians, which is used for trigonometric calculations in Python.
    sin_theta and cos_theta: The sine and cosine of the angle, respectively.
    tan_theta: The quotient of sin⁡(θ)sin(θ) and cos⁡(θ)cos(θ).
    cot_theta: The quotient of cos⁡(θ)cos(θ) and sin⁡(θ)sin(θ).
    tan_func: The tangent of the angle calculated using math.tan().
    cot_func: The cotangent of the angle calculated as the reciprocal of math.tan().
    Verification: The identities are verified by checking if the calculated quotients are close to the values obtained from the math functions, within a relative tolerance.
'''
