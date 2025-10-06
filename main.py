from call_handler import handle_inbound_call, handle_outbound_call

def main():
    print("AI Voice Agent Project Running (Dummy)")
    handle_inbound_call("+1234567890")
    handle_outbound_call("+0987654321")

if __name__ == "__main__":
    main()
