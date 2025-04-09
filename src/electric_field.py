import numpy as np
import matplotlib.pyplot as plt

k = 8.99e9 
q_pos = 1e-9 
q_neg = -1e-9 

pos_charge_pos = np.array([0.05, 0])
neg_charge_pos = np.array([-0.05, 0])

def calculate_potential(X, Y):
    r_pos = np.sqrt((X - pos_charge_pos[0])**2 + (Y - pos_charge_pos[1])**2)
    r_neg = np.sqrt((X - neg_charge_pos[0])**2 + (Y - neg_charge_pos[1])**2)
    V = k * (q_pos / r_pos + q_neg / r_neg)
    return V

def calculate_electric_field(V, spacing):
    Ey, Ex = np.gradient(-V, spacing, spacing)
    return Ex, Ey

def main():
    x = np.linspace(-0.2, 0.2, 100)
    y = np.linspace(-0.2, 0.2, 100)
    X, Y = np.meshgrid(x, y)

    V = calculate_potential(X, Y)
    Ex, Ey = calculate_electric_field(V, x[1]-x[0])

    plt.figure(figsize=(8, 6))
    levels = np.linspace(-500, 500, 20)
    contour = plt.contourf(X, Y, V, levels=levels, cmap='RdBu_r')
    plt.clim(-500, 500)
    
    plt.colorbar(label='Electric Potential (V)')
    plt.streamplot(X, Y, Ex, Ey, color='k', density=1.2)
    plt.xlabel('x (m)')
    plt.ylabel('y (m)')
    plt.title('Electric Field and Potential of an Electric Dipole')
    plt.plot(pos_charge_pos[0], pos_charge_pos[1], 'ro', label='Positive Charge')
    plt.plot(neg_charge_pos[0], neg_charge_pos[1], 'bo', label='Negative Charge')
    plt.legend()
    plt.axis('equal')
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    main()
