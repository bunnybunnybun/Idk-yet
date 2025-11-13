import libinput
from libinput import LibInput, ContextType, DeviveCapability

def setup_mouse_listener():
    li = LibInput(context=ContextType.PATH)
    li.path_add_udev("seat0")

    print("Boppidy bop bop")
    try:
        for event in li.get_event():
            if event.type == libinput.EventType.POINTER_MOTION:
                pevent = event.get_pointer_event()
                print(f"Mouse moved: x={pevent.dx:.lf}, y={peventt.dy:.lf}")
    except KeyboardInterrupt:
        pass
    finally:
        li.destroy()

if __name__ == "__main__":
    setup_mouse_listener()