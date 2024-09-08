''' 
The half-angle identities in trigonometry are used to express trigonometric functions of half-angles in terms of the original angle. Here are the half-angle identities:

    sin⁡(θ2)=±1−cos⁡(θ)2sin(2θ​)=±21−cos(θ)​
θ = theta sign, not a zero
​
cos⁡(θ2)=±1+cos⁡(θ)2cos(2θ​)=±21+cos(θ)​
​
tan⁡(θ2)=±1−cos⁡(θ)1+cos⁡(θ)tan(2θ​)=±1+cos(θ)1−cos(θ)​

    ​ or tan⁡(θ2)=sin⁡(θ)1+cos⁡(θ)tan(2θ​)=1+cos(θ)sin(θ)​ or tan⁡(θ2)=1−cos⁡(θ)sin⁡(θ)tan(2θ​)=sin(θ)1−cos(θ)​

Here is a Python script that calculates and verifies these half-angle identities for a given angle θθ:
'''


import math

def verify_half_angle_identities(angle_degrees):
    # Convert angle from degrees to radians
    angle_radians = math.radians(angle_degrees)
    half_angle_radians = angle_radians / 2
    
    # Calculate trigonometric functions for the given angle
    cos_theta = math.cos(angle_radians)
    sin_theta = math.sin(angle_radians)
    
    # Calculate trigonometric functions for the half angle
    sin_half_theta = math.sin(half_angle_radians)
    cos_half_theta = math.cos(half_angle_radians)
    tan_half_theta = math.tan(half_angle_radians)
    
    # Calculate half-angle identities
    sin_half_identity = math.sqrt((1 - cos_theta) / 2)
    cos_half_identity = math.sqrt((1 + cos_theta) / 2)
    tan_half_identity1 = math.sqrt((1 - cos_theta) / (1 + cos_theta))
    tan_half_identity2 = sin_theta / (1 + cos_theta)
    tan_half_identity3 = (1 - cos_theta) / sin_theta
    
    # Verify the identities
    results = {
        'sin(θ/2) = √((1 - cos(θ))/2)': math.isclose(sin_half_theta, sin_half_identity, rel_tol=1e-9),
        'cos(θ/2) = √((1 + cos(θ))/2)': math.isclose(cos_half_theta, cos_half_identity, rel_tol=1e-9),
        'tan(θ/2) = √((1 - cos(θ))/(1 + cos(θ)))': math.isclose(tan_half_theta, tan_half_identity1, rel_tol=1e-9),
        'tan(θ/2) = sin(θ)/(1 + cos(θ))': math.isclose(tan_half_theta, tan_half_identity2, rel_tol=1e-9),
        'tan(θ/2) = (1 - cos(θ))/sin(θ)': math.isclose(tan_half_theta, tan_half_identity3, rel_tol=1e-9)
    }
    
    return results

# Example usage
angle = 60  # degrees
results = verify_half_angle_identities(angle)

for identity, verified in results.items():
    print(f"{identity}: {'Verified' if verified else 'Not Verified'}")
'''
Explanation:

    angle_degrees: The angle in degrees for which the identities are verified.
    angle_radians: The angle in radians, which is used for trigonometric calculations in Python.
    half_angle_radians: The half angle (θ/2θ/2) in radians.
    cos_theta, sin_theta: The cosine and sine of the angle, respectively.
    sin_half_theta, cos_half_theta, tan_half_theta: The sine, cosine, and tangent of the half angle, respectively.
    sin_half_identity, cos_half_identity, tan_half_identity1, tan_half_identity2, tan_half_identity3: The values calculated using the half-angle identities.
    Verification: Each identity is verified by checking if the calculated values are close to the values obtained using the math functions, within a relative tolerance.
'''
