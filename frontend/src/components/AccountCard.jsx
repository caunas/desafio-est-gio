import {
    Card,
    CardContent,
    Typography,
    Button,
    Stack
} from "@mui/material";

export default function AccountCard({ account, onDelete }) {

    return (
        <Card>

            <CardContent>

                <Typography variant="h6">
                    {account.holder_name}
                </Typography>

                <Typography>
                    Conta: {account.account_type}
                </Typography>

                <Typography>
                    Saldo: R$ {account.balance}
                </Typography>

                <Typography>
                    ID: {account.id}
                </Typography>

                <Stack mt={2}>

                    <Button
                        color="error"
                        variant="outlined"
                        onClick={() => onDelete(account.id)}
                    >
                        Excluir
                    </Button>

                </Stack>

            </CardContent>

        </Card>
    );
}
