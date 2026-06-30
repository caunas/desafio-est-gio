import { AppBar, Toolbar, Typography } from "@mui/material";
import AccountBalanceIcon from "@mui/icons-material/AccountBalance";

export default function Header() {
    return (
        <AppBar position="static" elevation={1}>
            <Toolbar>
                <AccountBalanceIcon sx={{ mr: 2 }} />

                <Typography variant="h6">
                    Banco Digital
                </Typography>
            </Toolbar>
        </AppBar>
    );
}
