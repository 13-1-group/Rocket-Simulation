import Orbits

if __name__ == '__main__':

    def submenu_text_set(orbit_name: str) -> str:
        return f"""
            {orbit_name} orbit was chosen.
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

    if menu == 1:
        sub_menu = int(input(submenu_text_set("Elliptical")))
        if sub_menu == 1:
            e, a = 0.1, 2
            el = Orbits.Ellipsis(e, a)
            el.visualize()
        if sub_menu == 2:
            a = float(input('Enter the value of the semi-major axis a:\n'))
            e = float(input('Enter an eccentricity value e:\n'))
            if int(a) == 1:
                print('This eccentricity satisfies the trajectory of motion along the Barycentric Orbit!')
                el = Orbits.Ellipsis(e, a)
                el.visualize()
            else:
                el = Orbits.Ellipsis(e, a)
                el.visualize()

    if menu == 2:
        sub_menu = int(input(submenu_text_set("Hyperbolic")))
        if sub_menu == 1:
            e, a = 2, 10
            el = Orbits.Hyperbolic(e, a)
            el.visualize()
        if sub_menu == 2:
            a = float(input('Enter the value of the semi-major axis a:\n'))
            e = float(input('Enter an eccentricity value e:\n'))
            hyp = Orbits.Hyperbolic(e, a)
            hyp.visualize()

    if menu == 3:
        sub_menu = int(input(submenu_text_set("Parabolic")))
        if sub_menu == 1:
            p = 4
            pr = Orbits.Parabolic(4)
            pr.visualize()
        if sub_menu == 2:
            p = float(input('Enter the value of the focal semi-parameter of the trajectory p:\n'))
            pr = Orbits.Parabolic(p)
            pr.visualize()
