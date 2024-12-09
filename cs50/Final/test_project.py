from project import encrypt, open_cipher

def test_encrypt():
    assert encrypt('test') == '''
┌──────────────┐
│  #@+$###@    │
│              │
│              │
│              │
│              │
└──────────────┘
   wonkCIPHER

    '''