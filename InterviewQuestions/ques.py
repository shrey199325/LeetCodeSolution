"""
Quest:
MS1,2,3,4
Authenticate and authorize


Finance -- FinanceDashboard
Request
DB
Maintenance
Update
Finance - Billing
"""



"""


finance service
billing service
fin_dashboard service
MS5
MS6
MS7

API gateway:
    - Authorization and Authentication
    - SSL and TLS versions (with HTTP)
    - Reverse proxy
    - JWT Token

DB:
permissions:
Collection:
    "MS6": {
        "allowed": [MS7, finance, billing]
    }


                    Billing
     API GW         MS6


POST and Comments
Products and Users
Questions and Categories
    Physics: "what is light speed"
    Undefined: "define psychology"

- No of read and write operations
- Amount of data to be stored

POST
"How are you?"
    "good"
        "great"
COMMENT:
   id: ""
   post_id: ""
   maintext
   subcomment

post_id - POST
len(COMMENT -> post_id)
ans = []
postId = post_id from POST where comment=="how are you?"
comments = id from COMMENT where post_id==postId
if len(comments) > 3:
    ans.append(postId)
return query(* from POST where post_id in ans)

CORS
https 


single linked list - whether loop is present

1st 2nd
      1 - 2 - 3 - 4 - 1
"""


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        # self.visited = False


def is_loop_present(head):
    ptr1 = head
    ptr2 = head
    while ptr2 is not None and ptr2.next is not None:
        ptr1 = ptr1.next
        ptr2 = ptr2.next.next
        if id(ptr1) == id(ptr2):
            return True
    return False

