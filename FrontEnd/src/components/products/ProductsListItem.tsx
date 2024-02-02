import { Product, SearchedProduct } from "../../models/product.model";

type ProductsListItemProps = {
  product: Product | SearchedProduct;
};

export default function ProductsListItem({ product }: ProductsListItemProps) {
  return (
    <div
      style={{
        backgroundColor: "#f2f2f2",
        padding: "16px",
        gap: "4px",
        display: "flex",
        flexDirection: "column",
      }}
    >
      {/* First picture from pictures */}
      {"pictures" in product && product.pictures && (
        <div>
          <img
            style={{
              minHeight: "120px",
              backgroundColor: "#999",
              borderRadius: "8px",
              minWidth: "120px",
            }}
            width={100}
            src={
              product.pictures
                ? `http://localhost:8000${product.pictures[0]}`
                : undefined
            }
            alt={`${product.name}`}
          />
        </div>
      )}
      {/* Picture */}
      {"picture" in product && product.picture && (
        <div>
          <img
            style={{
              minHeight: "120px",
              backgroundColor: "#999",
              borderRadius: "8px",
              minWidth: "120px",
            }}
            width={100}
            src={`http://localhost:8000${product.picture}`}
            alt={`${product.name}`}
          />
        </div>
      )}
      {/* Product Name */}
      <div>
        <strong>{product.name}</strong>
      </div>
      {/* Product state */}
      <div style={{ display: "flex" }}>
        <div
          style={{
            backgroundColor: product.state === "in" ? "green" : "red",
            padding: "0px 8px",
            borderRadius: "4px",
            color: "white",
          }}
        >
          {product.state === "in" ? "In stock" : "Out of stock"}
        </div>
      </div>
      {/* Product categories */}
      {product.categories &&
        product.categories.map((category) => (
          <div
            style={{
              backgroundColor: "#444",
              padding: "0px 8px",
              borderRadius: "4px",
              color: "white",
            }}
          >
            {category.name}
          </div>
        ))}
    </div>
  );
}
