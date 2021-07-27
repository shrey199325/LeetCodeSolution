"""
Messaging app
SQL


Message:
    sender - sender_id
    receiver - receiver_id
    id -  (incremental id)
    text - str
    status - {sending, sent, delivered, read} == Failed/Read - read

User:
    id:
    name:
    phone_number:


Cache:
    User:
        id:
        status:
    Message:
        id: message_id (db)
        status: {sending, sent, delivered, read} (read)


U1 ----- LB ------ M1

U2 ------ LB ------ M2


                              Messaging   -----> Message
 U1, U2            LB         UserProfile  -----> User (C)
                              ContactRetrieval     (R)

                      Cache(User,Msg)

APIs:
ContactRetrieval: api/contactRetreival: payload: [pn1, pn2, pn3] = GET method -> {pn1: profile1, ...}
Messaging: api/message: payload: {u1_id, u2_id, message} = POST method -> {status} (sent)
                                                                       -> {u1, u2, message, msg_id}
                                                                       -> {msg_id, read}
UserProfile: api/user: payload: {name, phone_number} POST method -> Status code 200


M1 --------- U1
M2 --------- U2

Zookeeper
{
    M1: [u1, u2, u2]
    M2: [u10, u20, u30]
}



To be solved:
    https://leetcode.com/problems/count-of-smaller-numbers-after-self/
    Using: https://www.google.com/search?q=binary+index+tree&rlz=1C5CHFA_enIN908IN908&oq=binary+index+&aqs=chrome.1.69i57j0i457j0l6.4034j0j7&sourceid=chrome&ie=UTF-8


https://www.geeksforgeeks.org/search-element-sorted-matrix/
https://www.geeksforgeeks.org/search-in-row-wise-and-column-wise-sorted-matrix/
https://www.geeksforgeeks.org/search-element-in-a-spirally-sorted-matrix/?ref=rp


Binary indexed tree

    # int getSum(vector<int> btr, int index, int n)
    # {
    #     int ans = 0;
    #     while(index > 0 && index<=n)
    #     {
    #         ans+=btr[index];
    #         index -= (index & (-index));
    #     }
    #     return ans;
    # }

    # void update(vector<int> &btr, int index, int n , int val)
    # {
    #     while(index >= 0 && index<n)
    #     {
    #         btr[index]+=val;
    #         index += (index & (-index));
    #     }
    # }
"""