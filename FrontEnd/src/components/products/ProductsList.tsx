import ProductsListItem from "./ProductsListItem";
import { Product } from "../../models/product.model";

export default function ProductsList({ products }: { products: Product[] }) {
  return (
    <div
      style={{
        display: "flex",
        flexDirection: "column",
        gap: "16px",
        padding: "8px",
      }}
    >
      {/* Header title */}
      <div style={{ fontSize: "32px" }}>
        Products list{" "}
        <span style={{ fontSize: "22px", color: "#888" }}>
          ({products.length})
        </span>
      </div>

      {/* List of items */}
      <div
        style={{
          display: "flex",
          flexDirection: "row",
          flexWrap: "wrap",
          gap: "8px",
        }}
      >
        {products.map((product) => (
          <ProductsListItem key={product.id} product={product} />
        ))}
      </div>
    </div>
  );
}
