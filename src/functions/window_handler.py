from PySide6.QtCore import Qt

class WindowHandler:
    def __init__(self):
        # Dictionary untuk menyimpan instansi window yang aktif
        self._windows = {}

    def open_single_window(self, window_class, *args, **kwargs):
        """Membuka atau memfokuskan jendela tunggal."""
        existing_window = self._windows.get(window_class)

        # Jika jendela sudah ada dan masih terbuka, bawa ke depan
        if existing_window is not None and existing_window.isVisible():
            existing_window.raise_()
            existing_window.activateWindow()
            return existing_window

        # Buat instansi baru jika belum ada / sudah ditutup
        new_window = window_class(*args, **kwargs)
        new_window.setAttribute(Qt.WidgetAttribute.WA_DeleteOnClose)

        # Hapus dari dictionary saat jendela ditutup oleh user
        new_window.destroyed.connect(lambda: self._windows.pop(window_class, None))

        self._windows[window_class] = new_window
        new_window.show()
        return new_window