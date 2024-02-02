import { useState } from "react";
import BasePage from "./BasePage";
import { useLogin } from "../queries/user.query";
import { api } from "../axios";
import { useNavigate } from "react-router-dom";

function InputErrorMessage(props?: { message?: string }) {
  return props?.message ? (
    <div
      style={{
        backgroundColor: "red",
        color: "white",
        padding: "0px 8px",
        fontSize: "14px",
      }}
    >
      {props.message}
    </div>
  ) : (
    <></>
  );
}

export default function LoginPage() {
  const { login, loginError } = useLogin();
  const navigate = useNavigate();
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");

  function handleSubmitLogin() {
    login(
      { username, password },
      {
        onSuccess({ data }) {
          // Save access
          api.defaults.headers.common.Authorization = `Bearer ${data.access}`;
          // Redirect to main page
          navigate("/");
        },
      }
    );
  }

  return (
    <BasePage>
      <div
        style={{
          display: "flex",
          justifyContent: "center",
          alignItems: "center",
          flexDirection: "column",
          gap: "16px",
        }}
      >
        <div style={{ fontSize: "32px" }}>Login</div>
        <form
          style={{
            display: "flex",
            justifyContent: "center",
            alignItems: "center",
            flexDirection: "column",
            gap: "16px",
          }}
        >
          {/* Username */}
          <div>
            <div style={{ color: "#777" }}>Username</div>
            <input
              type="text"
              value={username}
              onChange={(e) => setUsername(e.target.value)}
              style={{
                backgroundColor: "white",
                color: "black",
                padding: "8px",
                borderRadius: "4px",
                width: "100%",
                marginBottom: "4px",
              }}
              autoFocus={true}
            />
            <InputErrorMessage message={loginError?.username} />
          </div>

          {/* Password */}
          <div>
            <div style={{ color: "#777" }}>Password</div>
            <input
              type="password"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              style={{
                backgroundColor: "white",
                color: "black",
                padding: "8px",
                borderRadius: "4px",
                width: "100%",
                marginBottom: "4px",
              }}
            />
            <InputErrorMessage message={loginError?.password} />
          </div>

          <InputErrorMessage message={loginError?.detail} />

          {/* Confirm btn */}
          <button
            type="submit"
            onClick={(e) => {
              e.preventDefault();
              handleSubmitLogin();
            }}
          >
            Confirm
          </button>
        </form>
      </div>
    </BasePage>
  );
}
