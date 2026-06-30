import { Grid } from "@mui/material";
import AccountCard from "./AccountCard";

export default function AccountList({ accounts, onDelete }) {

    return (
        <Grid container spacing={2}>

            {accounts.map((account) => (

                <Grid
                    item
                    xs={12}
                    md={6}
                    lg={4}
                    key={account.id}
                >

                    <AccountCard
                        account={account}
                        onDelete={onDelete}
                    />

                </Grid>

            ))}

        </Grid>
    );
}
