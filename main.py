import Orbits

if __name__ == '__main__':

    def submenu_text_set(orbit_name: str) -> str:
        return f"""
            Shoosen {orbit_name} Orbit.
            1 - set default values
            2 - set values by yourself
            """


    print(
        """
        1 - Elliptical Orbit
        2 - Hyperbolic Orbit
        3 - Parabolic Orbit
        """
    )
    menu = input('Select the trajectory of movement:\n')
    menu = int(menu)

    if menu is 1:
        sub_menu = int(input(submenu_text_set("Elliptical")))
        if sub_menu == 1:
            a, e = 0.1, 2
            el = Orbits.Ellipsis(a, e)
            el.visualize()
        if sub_menu == 2:
            a = float(input('Enter the value of the semi-major axis a:\n'))
            e = float(input('Enter an eccentricity value e:\n'))
            if (int(e) == 1):
                print('This eccentricity satisfies the trajectory of motion along the Barycentric Orbit!')
                el = Orbits.Ellipsis(a, e)
                el.visualize()
            else:
                el = Orbits.Ellipsis(a, e)
                el.visualize()

    if menu is 2:
        sub_menu = int(input(submenu_text_set("Hyperbolic")))
        if sub_menu == 1:
            a, e = 0.1, 10
            el = Orbits.Hyperbolic(a, e)
            el.visualize()
        if sub_menu == 2:
            a = float(input('Enter the value of the semi-major axis a:\n'))
            e = float(input('Enter an eccentricity value e:\n'))
            hyp = Orbits.Hyperbolic(a, e)
            hyp.visualize()

    if menu is 3:
        sub_menu = int(input(submenu_text_set("Parabolic")))
        if sub_menu == 1:
            p = 4
            pr = Orbits.Parabolic(4)
            pr.visualize()
        if sub_menu == 2:
            p = float(input('Enter the value of the focal semi-parameter of the trajectory p:\n'))
            pr = Orbits.Parabolic(p)
            pr.visualize()
