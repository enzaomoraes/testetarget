def descobrir_interruptores_simples():
    lampada_A = "fria"
    lampada_B = "fria"
    lampada_C = "fria"

    print("Ligue o interruptor A e espere um tempo para a lâmpada esquentar.")
    lampada_A = "quente"

    print("Desligue o interruptor A e ligue o interruptor B.")
    lampada_A = "morna"
    lampada_B = "acesa"

    print("\nAgora, vá até a sala das lâmpadas e veja o que aconteceu:")

    if lampada_B == "acesa":
        print("A lâmpada B está acesa. Logo, o interruptor B controla essa lâmpada.")

    if lampada_A == "morna":
        print("A lâmpada A está morna. Logo, o interruptor A controla essa lâmpada.")

    if lampada_C == "fria":
        print("A lâmpada C está fria. Logo, o interruptor C controla essa lâmpada.")

descobrir_interruptores_simples()
