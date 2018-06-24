CREATE TABLE sales.receipt
(
  "ID" text NOT NULL, -- Billing Reference
  "DATE" date NOT NULL, -- Date
  "FRIES" integer, -- Fries Qty
  "BURGER" integer, -- Burger Qty
  "FILET" integer, -- Filet Qty
  "CHICKEN" integer, -- Chicken Qty
  "CHEESE" integer, -- Cheese Qty
  "DRINKS" integer, -- Drinks Qty
  "SUBTOTAL" real, -- Sub Total
  "TAX" real, -- Tax
  "SERVICE_CHARGE" real, -- Service Charge
  "TOTAL_COST" real -- Total Cost
)
WITH (
  OIDS=FALSE
);
ALTER TABLE sales.receipt
  OWNER TO admin;
COMMENT ON TABLE sales.receipt
  IS 'Receipt Transaction Table';
COMMENT ON COLUMN sales.receipt."ID" IS 'Billing Reference';
COMMENT ON COLUMN sales.receipt."DATE" IS 'Date';
COMMENT ON COLUMN sales.receipt."FRIES" IS 'Fries Qty';
COMMENT ON COLUMN sales.receipt."BURGER" IS 'Burger Qty';
COMMENT ON COLUMN sales.receipt."FILET" IS 'Filet Qty';
COMMENT ON COLUMN sales.receipt."CHICKEN" IS 'Chicken Qty';
COMMENT ON COLUMN sales.receipt."CHEESE" IS 'Cheese Qty';
COMMENT ON COLUMN sales.receipt."DRINKS" IS 'Drinks Qty';
COMMENT ON COLUMN sales.receipt."SUBTOTAL" IS 'Sub Total';
COMMENT ON COLUMN sales.receipt."TAX" IS 'Tax';
COMMENT ON COLUMN sales.receipt."SERVICE_CHARGE" IS 'Service Charge';
COMMENT ON COLUMN sales.receipt."TOTAL_COST" IS 'Total Cost';
