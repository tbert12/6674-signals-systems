import numpy as np
from scipy import signal


def frequency(X, fs, segments_time, f0_propotion):
    """

    :param X: Señal de voz
    :return: Señal con modificacion
    """
    # 2. Localizar los picos de cada ciclo que conforman los segmentos sonoros.
    # 3. Segmentar la señal aplicando una ventana centrada en cada pico.
    # 4. Generar una nueva señal, alineando temporalmente y suma de los segmentos para obtener el nuevo período.
    new_x = np.copy(X)

    for sonorous_segment in segments_time:
        x_start = int(sonorous_segment[0] * fs)
        x_end = int(sonorous_segment[1] * fs)
        x_segment = X[x_start:x_end]
        peaks_idxs = signal.find_peaks_cwt(x_segment, np.arange(1, 100))

        # TODO: Usar frecuencia fundamental calculada?
        diffs = []
        prev = None
        for peak in peaks_idxs:
            if prev is not None:
                diffs.append(peak - prev)
            prev = peak
        mean_diff = np.mean(np.array(diffs))

        # Tomamos aproximadamente 2 periodos como ancho de ventana
        window_size = int(mean_diff * 2)

        windows = []
        for peak_idx in peaks_idxs[1:-1]:
            window = np.hanning(window_size)
            win_start = peak_idx - window_size // 2
            win_end = win_start + len(window)

            full_window = np.zeros(len(x_segment))
            _free = len(full_window[win_start:win_end])
            if len(window) <= _free:
                full_window[win_start:win_end] = window
            else:
                full_window[win_start:win_end] = window[:_free]
            windows.append(full_window)

        start_idx = np.nonzero(windows[0])[0][0]  # Tomo el primer lugar donde es distinto de 0
        end_idx = np.nonzero(windows[-1])[0][-1]  # Tomo ultimo lugar donde es distinto de 0

        starting_x_window = np.zeros(len(x_segment))
        starting_x_window[:start_idx] = 1  # Genero escalon para que la senal no se modifique en los extremos
        starting_x_window[end_idx:] = 1

        segmented_x = x_segment * starting_x_window

        periods_with_zeros = []
        for window in windows:
            # Genero cantidad de ventanas senales que toman solo valores en la ventana correspondiente
            period = x_segment * window  # ej. 000000011231241230000000000000000000000
            periods_with_zeros.append(period)

        periods = []
        for period_w_z in periods_with_zeros:
            # Me quedo solo con las ventanas
            period = np.trim_zeros(period_w_z)
            periods.append(period)

        result = segmented_x
        current_pos = start_idx
        """
        for period in periods:
            new_period_with_zeros = np.zeros(len(x_segment))
            new_period_with_zeros[current_pos:current_pos + len(period)] = period
            result += new_period_with_zeros
            current_pos += int(mean_diff * f0_propotion)
        """

        last_period = periods[-1]
        actual_period = 0
        while (current_pos + len(last_period)) < end_idx:
            # Mientras haya espacio, copiamos periodos, sino repido el ultimo
            actual_period = periods[0] if actual_period < len(periods) else last_period
            new_period_with_zeros = np.zeros(len(x_segment))
            new_period_with_zeros[current_pos:current_pos + len(periods)] = actual_period
            result += new_period_with_zeros
            current_pos += int(mean_diff * f0_propotion)

        new_x[x_start:x_end] = result  # Remplazo nuevos valores de la senal con distinta f0

    return new_x


def duration(X, fs, segments_time, time_proportion):
    # Realizo lo mismo que el anterior pero en los segmentos tengo que extenderlos o contraerlos
    # Si es menor el tiempo. Quito ventanas. Si es mayor repido
    pass
