import speedtest

def speed_test():
    st = speedtest.Speedtest()
    st.get_best_server()

    download_speed = st.download() / 10**6  # in Megabit pro Sekunde
    upload_speed = st.upload() / 10**6  # in Megabit pro Sekunde

    return download_speed, upload_speed

if __name__ == "__main__":
    download_speed, upload_speed = speed_test()
    print(f"Download-Geschwindigkeit: {download_speed:.2f} Mbps")
    print(f"Upload-Geschwindigkeit: {upload_speed:.2f} Mbps")
