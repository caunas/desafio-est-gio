import { useEffect, useState } from "react";

import {
    Container,
    Grid,
    Snackbar,
    Alert,
    CircularProgress,
    Typography
} from "@mui/material";

import Header from "./components/Header";
import AccountForm from "./components/AccountForm";
import OperationCard from "./components/OperationCard";
import TransferCard from "./components/TransferCard";
import AccountList from "./components/AccountList";

import api from "./api/api";

import "./App.css";

export default function App() {

    const [accounts, setAccounts] = useState([]);
    const [loading, setLoading] = useState(false);

    const [snackbar, setSnackbar] = useState({
        open: false,
        severity: "success",
        message: ""
    });

    function showMessage(message, severity = "success") {
        setSnackbar({
            open: true,
            severity,
            message
        });
    }

    async function loadAccounts() {

        setLoading(true);

        try {

            const response = await api.get("/api/account/all");
            setAccounts(response.data);

        } catch {

            showMessage("Erro ao carregar contas.", "error");

        }

        setLoading(false);
    }

    useEffect(() => {
        loadAccounts();
    }, []);

    async function createAccount(data) {

        try {

            const endpoint =
                data.type === "checking"
                    ? "/api/account/checking"
                    : "/api/account/saving";

            await api.post(endpoint, {
                holder_name: data.holder_name,
                initial_balance: data.initial_balance
            });

            showMessage("Conta criada!");

            loadAccounts();

        } catch {

            showMessage("Erro ao criar conta.", "error");

        }
    }

    async function deposit({ accountId, amount }) {

        try {

            await api.post(
                `/api/operations/deposit?account_id=${accountId}&amount=${amount}`
            );

            showMessage("Depósito realizado!");

            loadAccounts();

        } catch {

            showMessage("Erro no depósito.", "error");

        }
    }

    async function withdraw({ accountId, amount }) {

        try {

            await api.post(
                `/api/operations/withdraw?account_id=${accountId}&amount=${amount}`
            );

            showMessage("Saque realizado!");

            loadAccounts();

        } catch {

            showMessage("Erro no saque.", "error");

        }
    }

    async function transfer({ fromId, toId, amount }) {

        try {

            await api.post(
                `/api/operations/transfer?from_id=${fromId}&to_id=${toId}&amount=${amount}`
            );

            showMessage("Transferência realizada!");

            loadAccounts();

        } catch {

            showMessage("Erro na transferência.", "error");

        }
    }

    async function deleteAccount(id) {

        try {

            await api.delete(`/api/account/accounts/${id}`);

            showMessage("Conta excluída!");

            loadAccounts();

        } catch {

            showMessage("Erro ao excluir.", "error");

        }
    }

    return (
        <>
            <Header />

            <Container maxWidth="lg" sx={{ mt: 4, mb: 4 }}>

                <Grid container spacing={3}>

                    <Grid item xs={12} md={4}>
                        <AccountForm onCreate={createAccount} />
                    </Grid>

                    <Grid item xs={12} md={4}>
                        <OperationCard
                            title="Depositar"
                            buttonText="Depositar"
                            onSubmit={deposit}
                        />
                    </Grid>

                    <Grid item xs={12} md={4}>
                        <OperationCard
                            title="Sacar"
                            buttonText="Sacar"
                            onSubmit={withdraw}
                        />
                    </Grid>

                    <Grid item xs={12}>
                        <TransferCard
                            onTransfer={transfer}
                        />
                    </Grid>

                    <Grid item xs={12}>
                        <Typography
                            variant="h5"
                            mb={2}
                        >
                            Contas
                        </Typography>

                        {
                            loading
                                ? <CircularProgress />
                                : (
                                    <AccountList
                                        accounts={accounts}
                                        onDelete={deleteAccount}
                                    />
                                )
                        }

                    </Grid>

                </Grid>

            </Container>

            <Snackbar
                open={snackbar.open}
                autoHideDuration={2500}
                onClose={() =>
                    setSnackbar({
                        ...snackbar,
                        open: false
                    })
                }
            >

                <Alert severity={snackbar.severity}>
                    {snackbar.message}
                </Alert>

            </Snackbar>

        </>
    );
}
