from app.settings.connectdb import Firebase
# from app.functions.face import Ids



class GetgaceandData:
  def __init__(self):
    self.ref=Firebase().ref
    # self.id=Ids().id
    self.idsref=Firebase().idsref
    self.bucket=Firebase().bucket
  def get_data_by_key(self):
    return self.ref.child(self.id).get()
  def get_picture(self):
    return self.bucket.get_blob(f"faceappimage/{self.id}")
  
  def get_data_by_child(self):
    return self.ref.order_by_child("status").equal_to("Present").get()