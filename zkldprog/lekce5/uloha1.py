def circle_area(d):
    r=d/2
    return 3.14*r**2
print(circle_area(0.20))
def tube_cross_section(d_out, d_in):
    return(circle_area(d_out)-circle_area(d_in))
print(tube_cross_section(0.20,0.10))
def tube_mass(d_out, d_in, length, density=7850):
    return(density*tube_cross_section(d_out,d_in)*length)
print(tube_mass(0.05,0.04,2))
print(tube_mass(0.060, 0.050, 6))                # ocelová trubka: ≈ 40.69 kg
print(tube_mass(0.060, 0.050, 6, density=2700))  # hliníková: ≈ 14.00 kg
