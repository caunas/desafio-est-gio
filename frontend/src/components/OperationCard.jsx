import { useState } from "react";
import {
    Paper,
    Typography,
    TextField,
    Stack,
    Button
} from "@mui/material";

export default function OperationCard({
    title,
    buttonText,
    onSubmit
}) {

    const [accountId, setAccountId] = useState("");
    const [amount, setAmount] = useState("");

    const handleClick = () => {

        if (!accountId || !amount) return;

        onSubmit({
            accountId: Number(accountId),
            amount: Number(amount)
        });

        setAccountId("");
        setAmount("");
    };

    return (
        <Paper sx={{ p: 3 }}>

            <Typography variant="h6" mb={2}>
                {title}
            </Typography>

            <Stack spacing={2}>

                <TextField
                    label="Conta"
                    type="number"
                    value={accountId}
                    onChange={(e) => setAccountId(e.target.value)}
                />

                <TextField
                    label="Valor"
                    type="number"
                    value={amount}
                    onChange={(e) => setAmount(e.target.value)}
                />

                <Button
                    variant="contained"
                    onClick={handleClick}
                >
                    {buttonText}
                </Button>

            </Stack>

        </Paper>
    );
}
