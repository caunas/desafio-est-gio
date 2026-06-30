import { useState } from "react";
import {
    Paper,
    Typography,
    TextField,
    Button,
    Stack
} from "@mui/material";

export default function TransferCard({ onTransfer }) {

    const [fromId, setFromId] = useState("");
    const [toId, setToId] = useState("");
    const [amount, setAmount] = useState("");

    const handleTransfer = () => {

        if (!fromId || !toId || !amount) return;

        onTransfer({
            fromId: Number(fromId),
            toId: Number(toId),
            amount: Number(amount)
        });

        setFromId("");
        setToId("");
        setAmount("");
    };

    return (
        <Paper sx={{ p: 3 }}>

            <Typography variant="h6" mb={2}>
                Transferência
            </Typography>

            <Stack spacing={2}>

                <TextField
                    label="Conta Origem"
                    type="number"
                    value={fromId}
                    onChange={(e) => setFromId(e.target.value)}
                />

                <TextField
                    label="Conta Destino"
                    type="number"
                    value={toId}
                    onChange={(e) => setToId(e.target.value)}
                />

                <TextField
                    label="Valor"
                    type="number"
                    value={amount}
                    onChange={(e) => setAmount(e.target.value)}
                />

                <Button
                    variant="contained"
                    onClick={handleTransfer}
                >
                    Transferir
                </Button>

            </Stack>

        </Paper>
    );
}
