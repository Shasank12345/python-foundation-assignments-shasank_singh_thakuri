import logging as log
import csv
import json

with open("day-04-python-foundations/orders.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["order_id", "item", "qty", "price"])
    writer.writerow(["1", "Keyboard", "2", "45.00"])
    writer.writerow(["2", "Mouse", "not_a_number", "15.00"])   
    writer.writerow(["3", "Monitor", "1", "-120.00"])         
    writer.writerow(["4", "USB Cable", "5", "4.50"])

print("orders.csv created (with 2 intentionally bad rows).")

def process_orders(csv_path, json_path, log_path):
    logger = log.getLogger("orders")
    logger.setLevel(log.INFO)
    if not logger.handlers:
        handler = log.FileHandler(log_path)
        formatter = log.Formatter("%(asctime)s - %(levelname)s - %(message)s")
        handler.setFormatter(formatter)
        logger.addHandler(handler)

    valid_rows = []
    num_valid = 0
    num_invalid = 0

    try:
        with open(csv_path, "r", newline="", encoding="utf-8") as c:
            reader = csv.DictReader(c)

            for row in reader:
                row_num = reader.line_num
                try:
                    qty_val = float(row["qty"])
                    price_val = float(row["price"])
                except ValueError as e:
                    logger.error(
                        f"Row {row_num}: could not convert qty/price ({row['qty']!r}, {row['price']!r}) - SKIPPED. Reason: {e}"
                    )
                    num_invalid += 1
                    continue

                if qty_val < 0 or price_val < 0:
                    logger.error(
                        f"Row {row_num}: negative qty or price - SKIPPED"
                    )
                    num_invalid += 1
                    continue

                total = qty_val * price_val
                enriched_row = {
                    "order_id": row["order_id"],
                    "item": row["item"],
                    "qty": int(qty_val) if qty_val.is_integer() else qty_val,
                    "price": price_val,
                    "total": int(total) if total.is_integer() else total,
                }
                valid_rows.append(enriched_row)
                num_valid += 1
                logger.info(
                    f"Row {row_num}: Successfully processed order {row['order_id']}."
                )

    except FileNotFoundError:
        logger.critical(f"Input file not found at path: {csv_path}")
        return (0, 0)
    finally: 
            logger.info("Finished reading input CSV")
        
    with open(json_path, "w") as jf:
        json.dump(valid_rows, jf, indent=4)

    return (num_valid, num_invalid)




result = process_orders("day-04-python-foundations/orders.csv", "day-04-python-foundations/orders_clean.json", "day-04-python-foundations/orders_pipeline.log")
print(result)

print("\n--- orders_clean.json ---")
with open("day-04-python-foundations/orders_clean.json") as f:
    print(f.read())

print("\n--- orders_pipeline.log ---")
with open("day-04-python-foundations/orders_pipeline.log") as f:
    print(f.read())



