
#Import libraries
import numpy as np
import matplotlib.pyplot as plt




# Data from the COBE satellite
# Measured data: wavelength is in millimetres.
#measured_lambda=np.array([4.405286344,3.676470588,3.144654088,\
#2.754820937,2.450980392,2.004008016,1.834862385,1.377410468,\
#0.881834215,0.468823254],float)
# Measured data: intensity in W m**-2 m**-1 sr**-1
measured_intensity=np.array([3.10085E-05,5.53419E-05,8.8836E-05,\
0.000129483,0.000176707,0.000284786,0.00034148,0.000531378,\
0.000561909,6.16936E-05],float)







def radiation(wavelength,temp):
    # Define constants needed:
    h = 6.626e-34 #Planck constnat in Js
    c = 2.998e+8  #Speed of light in m/s
    k = 1.381e-23 #Boltzmann constant in J/K

    # Determine the spectrum intensities
    first_term=(2*h*c*c)/(wavelength**5)
    arg_of_exp=h*c/(wavelength*k*temp)
    B_value=first_term*(1/(np.exp(arg_of_exp)-1))
    # Return array of intensity values
    return B_value


# Ask to guess the CMB temperature (in Kelvin)
while True:
    temperature=float(input("Guess the CMB temperature (in Kelvin), or type zero to exit:" ))
    if temperature == 0:
        print ("You exeted the loop")
        break
    else:
        print ("The temperature you entered is:", temperature, "K")

    # Define the wavelength range in millimetres
    lambda_range=np.linspace(0.1,5.0,50,endpoint=True)
    # convert to metres
    lambda_range_metres=lambda_range*1e-3

    # The function below calculates the black-body spectrum
    # intensities for a given temperature

        # Define constants needed:
    h = 6.626e-34 #Planck constnat in Js
    c = 2.998e+8  #Speed of light in m/s
    k = 1.381e-23 #Boltzmann constant in J/K

    wavelength = lambda_range_metres
    temp = temperature
    # Determine the spectrum intensities
    first_term=(2*h*c*c)/(wavelength**5)
    arg_of_exp=h*c/(wavelength*k*temp)
    B_value=first_term*(1/(np.exp(arg_of_exp)-1))
    # Return array of intensity values
    

      # Calculate the RMSD 
    root_mean_square_dev = (sum((B_value - measured_intensity)**2)/len(B_value))**0.5
    print ("The RMSD is:", root_mean_square_dev)
    
    # Assign values from the user-defined function to an
    # array of intensity values
    intensities=radiation(lambda_range_metres,temperature)
    
    # Plot the intensity values against the wavelength in millimetres
    plt.plot(lambda_range,intensities)
    plt.show()
