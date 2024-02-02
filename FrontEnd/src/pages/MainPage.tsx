import BasePage from "./BasePage";
import ProductsList from "../components/products/ProductsList";
import { useGetProducts } from "../queries/product.query";
import { Link } from "react-router-dom";
import { useGetUserProfile, useLogin } from "../queries/user.query";
import { useEffect, useState } from "react";

export default function MainPage() {
  const [search, setSearch] = useState("");
  const { products, isGettingProducts, refetchProducts } =
    useGetProducts(search);
  const { userProfile, isLogged } = useGetUserProfile();
  const { logout } = useLogin();

  useEffect(() => {
    refetchProducts();
  }, [search]);

  if (isGettingProducts) return <div>Loading products...</div>;

  const isLoggedIn = isLogged();

  function handleLogout() {
    logout();
    refetchProducts();
  }

  return (
    <BasePage>
      {/* Header */}
      <div
        style={{
          display: "flex",
          flexDirection: "row",
          justifyContent: "space-between",
          alignItems: "center",
          padding: "0 8px",
        }}
      >
        {/* Products searcher */}
        <input
          value={search}
          onChange={(e) => setSearch(e.target.value)}
          type="text"
          placeholder="Search products..."
          style={{
            backgroundColor: "white",
            color: "black",
            padding: "8px",
            borderRadius: "4px",
          }}
        />
        {/* Login / Logout */}
        <div
          style={{
            display: "flex",
            flexDirection: "row",
            justifyContent: "end",
            alignItems: "center",
            gap: 4,
          }}
        >
          {isLoggedIn && (
            <div>
              Bienvenido <strong>{userProfile?.username}</strong>
            </div>
          )}
          <button onClick={isLoggedIn ? handleLogout : undefined}>
            {isLoggedIn ? (
              <div>Logout</div>
            ) : (
              <Link style={{ color: "white" }} to={`login/`}>
                Login
              </Link>
            )}
          </button>
        </div>
      </div>

      {/* Products list */}
      {products && <ProductsList products={products} />}
    </BasePage>
  );
}
