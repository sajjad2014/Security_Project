class CA:
    def __init__(self):
        self.id_pub_key_pair = {}
        self.id_certificate_pair = {}
        self.id_randnum_pair = {} #for keys in the process of verification
        #todo generate and save self public and private key
        self.pub_key = None
        self.pri_key = None

    def verify_id(self, id, pub_key):
        #todo send an email to id and send an encoded message
        pass

    def check_pub_key(self, id, randnum):
        if id in self.id_randnum_pair:
            if self.id_randnum_pair[id] == randnum:
                #todo create a certificate and send it back and
                # update id_pub_key_pair and id_certificate_pair
                pass
        #todo send a message that the verification failed or not idk

    def get_certificate(self, id):
        if id in self.id_certificate_pair:
            return self.id_certificate_pair[id]
        #todo convert to appropriate message