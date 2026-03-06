from ethereum_connector import register_batch, transfer_batch, get_batch

print(register_batch("B1001", "Covishield", "Serum Institute"))
print(transfer_batch("B1001", "Kerala Distributor"))
print(get_batch("B1001"))