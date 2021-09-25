import dropbox
class TransferData :
  def __init__ (self, accesstoken) :
    self.accesstoken = accesstoken
  def upload (self, filefrom, fileto) :
    dbx = dropbox.Dropbox(self.accesstoken)
    with open(filefrom, "rb") as f :
      dbx.files_upload(f.read(),fileto)

def main() :
  accesstoken = "VDVCZuwQVm8AAAAAAAAAATA7feGNQeawWXr2H37iJIzx-mLDuccP3O2RRfT-o5dU"
  data = TransferData(accesstoken)
  filefrom = "File.jpg"
  fileto = '/Project 101/File.jpg'
  data.upload(filefrom, fileto)

if __name__ == "__main__" :
  main()