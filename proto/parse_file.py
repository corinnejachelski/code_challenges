import struct


def parse_log(log_data):
    with open(log_data, 'rb') as f:

        #create empty list to store records
        log_records = []

        #parse header
        header = f.read(9)
        #'!' indicates network byte order
        parsed_header = struct.unpack('!ccccBI', header)

        #read first byte in string to parse record type enum
        byte = f.read(1)
        parsed_byte = struct.unpack('!B', byte)


        while byte:
            #if type is debit or credit, need to parse additional 8 byte (float64) amount in dollars
            if parsed_byte[0] == 0 or parsed_byte[0] == 1:
                #record contains 1 byte record type (B), 4 byte (uint32) Unix timestamp(I), 
                #8 byte (uint64) user ID(Q), 8 byte (float64) amount in dollars (d) - 21 byte record
                byte = byte + f.read(20)
                record = struct.unpack('!BIQd', byte)

            else:
                #record contains 1 byte record type (B), 4 byte (uint32) Unix timestamp(I), 
                #8 byte (uint64) user ID(Q) - 13 byte record
                byte = byte + f.read(12)
                record = struct.unpack('!BIQ', byte)
            
            log_records.append(record)

            #increment to read next record enum type
            byte = f.read(1)
            if byte:
                parsed_byte = struct.unpack('!B', byte)

        print(log_records)

        return log_records

def get_log_stats():

    #log_records is a list of tuples
    #order of data in log_records: (record_type, timestamp, user_id, dollar_amount*) 
    #*dollar amount depends on record type
    #sample line in log_records: (0, 1393108945, 4136353673894269217, 604.274335557087)
    log_records = parse_log('txnlog.dat')

    total_credit_amount = 0
    total_debit_amount = 0
    autopays_started = 0
    autopays_ended = 0
    user_balance = 0

    for record in log_records:
        if record[0] == 1:
            total_credit_amount += record[3]
        if record[0] == 0:
            total_debit_amount += record[3]
        if record[0] == 3:
            autopays_started += 1
        if record[0] == 4:
            autopays_ended += 1
        if record[2] == 2456938384156277127 and record[0] == 0 or record[0] == 1:
            user_balance = record [3]

    stats = f'''total credit amount={total_credit_amount} 
    total debit amount={total_debit_amount}
    autopays started={autopays_started}
    autopays ended={autopays_ended}
    balance for user 2456938384156277127={user_balance}'''

    print(stats)
    

if __name__ == "__main__":
    get_log_stats()

