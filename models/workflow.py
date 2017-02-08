class EmailItem(object):
    def __init__(self, item):
        for child in item:
            if 'to' in child.tag:
                self.to = child.text
            elif 'subject' in child.tag:
                self.subject = child.text
            elif 'body' in child.tag:
                self.body = child.text

    def __display__(self):
        print("To: " + self.to + '\n' + "Subject: " + self.subject + '\n' + "Body: " + self.body)

