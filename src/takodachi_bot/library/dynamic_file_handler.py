import takodachi_bot.configs as Configs
import os
from datetime import datetime
from logging import FileHandler


class DynamicFileHandler(FileHandler):
    def __init__(self, log_folder_name="", mode='a', encoding=None, delay=True):
        log_folder_name = log_folder_name.strip("'\"")
        filename = os.path.join(Configs.LOG_DIRECTORY, log_folder_name, self.get_current_date() + '.log')
        super().__init__(filename, mode, encoding, delay)

    def _open(self):
        """ 
        🌟 覆寫底層開檔邏輯：
        只有當程式第一次呼叫 logger.info() 觸發寫入時，才會進來這裡。
        這時我們才動手建立資料夾，時間點最精準、最安全！
        """
        os.makedirs(os.path.dirname(self.baseFilename), exist_ok=True)
        return super()._open()

    def get_current_date(self):
        return datetime.now().strftime('%Y-%m-%d')
