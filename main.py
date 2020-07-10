from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
import webbrowser

def any_Function(instance):

    webbrowser.open('https://www.youtube.com/results?search_query=skymatix')

def any_Function1(instance):

    webbrowser.open('https://www.facebook.com/groups/SAFSim/')

def any_Function2(instance):

    webbrowser.open('https://www.x-aviation.com/catalog/')

def any_Function3(instance):

    webbrowser.open('https://navigraph.com/home')

def any_Function4(instance):

    webbrowser.open('https://forums.x-plane.org/')

def any_Function5(instance):

    webbrowser.open('https://www.prepar3d.com/')

def any_Function6(instance):

    webbrowser.open('https://rexsimulations.com/')

def any_Function7(instance):

    webbrowser.open('https://www.thresholdx.net/')

def any_Function8(instance):

    webbrowser.open('https://www.flightsimulator.com/')

def any_Function9(instance):

    webbrowser.open('https://orbxdirect.com/product/orbxlibs-xp11')

def any_Function10(instance):

    webbrowser.open('https://www.youtube.com/watch?v=fkvmlbJXAq4')

def any_Function11(instance):

    webbrowser.open('https://secure.simmarket.com/default-en.html')

def any_Function12(instance):

    webbrowser.open('https://www.siminnovations.com/')

def any_Function13(instance):

    webbrowser.open('https://www.nmgsimulations.co.za/')

def any_Function14(instance):

    webbrowser.open('https://forums.x-pilot.com/')

def any_Function15(instance):

    webbrowser.open('https://forums.x-pilot.com/forums/topic/10463-livery-list-requests/')

def any_Function16(instance):

    webbrowser.open('https://www.facebook.com/GafferSimulations/')

def any_Function17(instance):

    webbrowser.open('https://gateway.x-plane.com/')

def any_Function18(instance):

    webbrowser.open('https://www.prepar3d.com/SDKv4/prepar3d/world/scenery_library/scenery_library_overview.html')

def any_Function19(instance):

    webbrowser.open('https://www.captainsim.com/')


def any_Function20(instance):
    webbrowser.open('https://www.justflight.com/')


def any_Function21(instance):
    webbrowser.open('https://www.freewarescenery.com/fsx.html')


def any_Function22(instance):
    webbrowser.open('https://simtoolkitpro.co.uk/')


def any_Function23(instance):
    webbrowser.open('https://www.simbrief.com/home/')


def any_Function24(instance):
    webbrowser.open('https://albar965.github.io/')


def any_Function25(instance):
    webbrowser.open('https://forums.x-plane.org/index.php?/files/file/48742-joinfs/')


def any_Function26(instance):
    webbrowser.open('https://forums.x-plane.org/index.php?/files/file/42357-virtual-first-officer/')


def any_Function27(instance):
    webbrowser.open('http://www.prepar3d.com/SDKv2/LearningCenter/getting_started/multiplayer/multiplayer_sharing_an_aircraft.html')


def any_Function28(instance):
    webbrowser.open('http://www.multicrewxp.com/Downloads.html')


def any_Function29(instance):
    webbrowser.open('https://library.avsim.net/')


def any_Function30(instance):

    webbrowser.open('https://www.prepar3d.com/vehicles/')

def any_Function31(instance):

    webbrowser.open('https://sky4crew.com/smartcopilot/')

def any_Function32(instance):

    webbrowser.open('https://forums.x-plane.org/index.php?/files/file/38445-flywithlua-ng-next-generation-edition-for-x-plane-11-win-lin-mac/')

def any_Function33(instance):

    webbrowser.open('http://www.xpluginsdk.org/python_interface_latest_downloads.htm')

def any_Function34(instance):

    webbrowser.open('http://jardesign.org/')


def any_Function35(instance):
    webbrowser.open('https://developer.x-plane.com/tools/worldeditor/')


def any_Function36(instance):
    webbrowser.open('https://www.opensceneryx.com/')


def any_Function37(instance):
    webbrowser.open('https://forums.x-plane.org/index.php?/files/file/34155-airport-navigator/')


def any_Function38(instance):
    webbrowser.open('www.google.com')


def any_Function39(instance):
    webbrowser.open('https://developer.x-plane.com/tools/datarefeditor/')


def any_Function40(instance):
    webbrowser.open('')


def any_Function41(instance):
    webbrowser.open('')



class SimInfoApp(App):
    def build(self):
        layout = GridLayout(cols=3, row_force_default=True, row_default_height=40,
                            spacing=5, padding=10)
        btn1 = Button(text="SkyMatix YouTube (Zibo)")
        btn1.bind(on_press=any_Function)

        btn2 = Button(text="South African Flight Simmers\nRequires Join Invitation (FB)")
        btn2.bind(on_press=any_Function1)

        btn3 = Button(text="X-Aviation")
        btn3.bind(on_press=any_Function2)

        btn4 = Button(text="NaviGraph (Account)")
        btn4.bind(on_press=any_Function3)

        btn5 = Button(text="Xplane Org")
        btn5.bind(on_press=any_Function4)

        btn6 = Button(text="Prepar 3D Home")
        btn6.bind(on_press=any_Function5)

        btn7 = Button(text="RexTexture Direct Pre 3D")
        btn7.bind(on_press=any_Function6)

        btn8 = Button(text="Threshold")
        btn8.bind(on_press=any_Function7)

        btn9 = Button(text="MicroSoft Flight Simulator Home")
        btn9.bind(on_press=any_Function8)

        btn10 = Button(text="Orbex (Airports & Scenery)")
        btn10.bind(on_press=any_Function9)

        btn11 = Button(text="Ortho4XP & Pre3D (Scenery)\nYouTube")
        btn11.bind(on_press=any_Function10)

        btn12 = Button(text="SimMarket")
        btn12.bind(on_press=any_Function11)

        btn13 = Button(text="Air Manager")
        btn13.bind(on_press=any_Function12)

        btn14 = Button(text="NMG Simulations")
        btn14.bind(on_press=any_Function13)

        btn15 = Button(text="X-Pilot.com")
        btn15.bind(on_press=any_Function14)

        btn16 = Button(text="Ixeg 733 Liveries")
        btn16.bind(on_press=any_Function15)

        btn17 = Button(text="GAFFER Simulations")
        btn17.bind(on_press=any_Function16)

        btn18 = Button(text="The X-Plane Scenery Gateway")
        btn18.bind(on_press=any_Function17)

        btn19 = Button(text="Prepard3d Scenery\nLibrary Instillation")
        btn19.bind(on_press=any_Function18)

        btn20 = Button(text="CaptainSim")
        btn20.bind(on_press=any_Function19)

        btn21 = Button(text="JustFlight")
        btn21.bind(on_press=any_Function20)

        btn22 = Button(text="Fsx & Pre3d Scenery's")
        btn22.bind(on_press=any_Function21)

        btn23 = Button(text="SimTool Kit Pro")
        btn23.bind(on_press=any_Function22)

        btn24 = Button(text="SimBrief")
        btn24.bind(on_press=any_Function23)

        btn25 = Button(text="Little Nav Map")
        btn25.bind(on_press=any_Function24)

        btn26 = Button(text="Join Fs")
        btn26.bind(on_press=any_Function25)

        btn27 = Button(text="Xplane First Officer")
        btn27.bind(on_press=any_Function26)

        btn28 = Button(text="Pre3D Share Cockpit")
        btn28.bind(on_press=any_Function27)

        btn29 = Button(text="Pre3d Multi crew Copilot")
        btn29.bind(on_press=any_Function28)

        btn30 = Button(text="Avsim")
        btn30.bind(on_press=any_Function29)

        btn31 = Button(text="Pre3d Vehicle Addons")
        btn31.bind(on_press=any_Function30)

        btn32 = Button(text="Smart Co-pilot Xplane 11")
        btn32.bind(on_press=any_Function31)

        btn33 = Button(text="Fly With Lua ")
        btn33.bind(on_press=any_Function32)

        btn34 = Button(text="Python")
        btn34.bind(on_press=any_Function33)

        btn35 = Button(text="JarDesigns")
        btn35.bind(on_press=any_Function34)

        btn36 = Button(text="WorldEditor")
        btn36.bind(on_press=any_Function35)

        btn37 = Button(text="OpenScenery")
        btn37.bind(on_press=any_Function36)

        btn38 = Button(text="Airport Navigator Xplane 11")
        btn38.bind(on_press=any_Function37)

        btn39 = Button(text="GOOGLE Search")
        btn39.bind(on_press=any_Function38)

        btn40 = Button(text="Data Ref Xplane 11")
        btn40.bind(on_press=any_Function39)

        btn41 = Button(text="App Designed By:\nbrendenevy@gmail.com")

        layout.add_widget(btn1)
        layout.add_widget(btn2)
        layout.add_widget(btn3)
        layout.add_widget(btn4)
        layout.add_widget(btn5)
        layout.add_widget(btn6)
        layout.add_widget(btn7)
        layout.add_widget(btn8)
        layout.add_widget(btn9)
        layout.add_widget(btn10)
        layout.add_widget(btn11)
        layout.add_widget(btn12)
        layout.add_widget(btn13)
        layout.add_widget(btn14)
        layout.add_widget(btn15)
        layout.add_widget(btn16)
        layout.add_widget(btn17)
        layout.add_widget(btn18)
        layout.add_widget(btn19)
        layout.add_widget(btn20)
        layout.add_widget(btn21)
        layout.add_widget(btn22)
        layout.add_widget(btn23)
        layout.add_widget(btn24)
        layout.add_widget(btn25)
        layout.add_widget(btn26)
        layout.add_widget(btn27)
        layout.add_widget(btn28)
        layout.add_widget(btn29)
        layout.add_widget(btn30)
        layout.add_widget(btn31)
        layout.add_widget(btn32)
        layout.add_widget(btn33)
        layout.add_widget(btn34)
        layout.add_widget(btn35)
        layout.add_widget(btn36)
        layout.add_widget(btn37)
        layout.add_widget(btn38)
        layout.add_widget(btn39)
        layout.add_widget(btn40)
        layout.add_widget(btn41)

        return layout

SimInfoApp().run()
