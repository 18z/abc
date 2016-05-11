import notify2
import pyperclip

notify2.init('Sixense')

n = notify2.Notification("Sixense",
                         pyperclip.paste(),
                         "notification-message-im"   # Icon name
                        )
n.show()
