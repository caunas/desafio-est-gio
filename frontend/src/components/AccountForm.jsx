import { useState } from "react";
import {
    Paper,
    Typography,
    TextField,
    RadioGroup,
    FormControlLabel,
    Radio,
    Button,
    Stack
} from "@mui/material";

export default function AccountForm({ onCreate }) {

    const [holderName, setHolderName] = useState("");
    const [balance, setBalance] = useState("");
    const [type, setType] = useState("checking");

    const handleSubmit = () => {

        if (!holderName || !balance) return;

        onCreate({
            holder_name: holderName,
            initial_balance: Number(balance),
            type
        });

        setHolderName("");
        setBalance("");
    };

    return (
        <Paper sx={{ p: 3 }}>

            <Typography variant="h6" mb={2}>
                Criar Conta
            </Typography>

            <Stack spacing={2}>

                <TextField
                    label="Nome do Titular"
                    value={holderName}
                    onChange={(e) => setHolderName(e.target.value)}
                    fullWidth
                />

                <TextField
                    label="Saldo Inicial"
                    type="number"
                    value={balance}
                    onChange={(e) => setBalance(e.target.value)}
                />

                <RadioGroup
                    value={type}
                    onChange={(e) => setType(e.target.value)}
                >
                    <FormControlLabel
                        value="checking"
                        control={<Radio />}
                        label="Conta Corrente"
                    />

                    <FormControlLabel
                        value="saving"
                        control={<Radio />}
                        label="Conta Poupança"
                    />
                </RadioGroup>

                <Button
                    variant="contained"
                    onClick={handleSubmit}
                >
                    Criar Conta
                </Button>

            </Stack>

        </Paper>
    );
}
